import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from instagrapi import Client
from instagrapi.mixins.note import NoteAudience

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TELEGRAM_BOT_TOKEN = "Your_Bot_Token"
SESSION_FILE = "session.json"

cl = Client()
try:
    cl.load_settings(SESSION_FILE)
    cl.login_by_sessionid()
    logging.info("Logged into Instagram successfully.")
except Exception as e:
    logging.error(f"Failed to load session: {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bot is online!\n\n"
        "Send:\n"
        "/note <song name> | <caption text>\n\n"
        "Example:\n"
        "/note golden brown | hi"
    )

async def post_music_note(update: Update, context: ContextTypes.DEFAULT_TYPE):
    input_text = " ".join(context.args)
    if not input_text or "|" not in input_text:
        await update.message.reply_text("Usage: /note <song query> | <caption text>")
        return

    parts = input_text.split("|", 1)
    song_query = parts[0].strip()
    note_caption = parts[1].strip()

    if len(note_caption) > 60:
        await update.message.reply_text("Caption exceeds 60 characters limit.")
        return

    await update.message.reply_text(f"Searching Instagram catalog for: '{song_query}'...")

    def execute_note_post():
        selected_track = None
        alacorn_id = None

        # Method 1: Full Instagram Song Catalog Search
        try:
            tracks = cl.search_music(song_query)
            if tracks:
                selected_track = tracks[0]  # Get the top matching search result
        except Exception as e:
            logging.error(f"search_music error: {e}")

        # Method 2: Fallback to Note Candidate Browser
        if not selected_track:
            try:
                music_data = cl.notes_music_browser()
                alacorn_id = music_data.get("alacorn_session_id")
                items = music_data.get("items", [])
                for item in items:
                    track_info = item.get("playlist", {}).get("preview_items", [{}])[0].get("track")
                    if track_info:
                        title = str(track_info.get("title", "")).lower()
                        artist = str(track_info.get("display_artist", "")).lower()
                        if song_query.lower() in title or song_query.lower() in artist:
                            selected_track = track_info
                            break
            except Exception as e:
                logging.error(f"notes_music_browser error: {e}")

        if not selected_track:
            return None, f"No track found on Instagram matching '{song_query}'."

        # Post the Music Note
        note = cl.create_music_note(
            track=selected_track,
            text=note_caption,
            audience=NoteAudience.MUTUAL_FOLLOWERS,
            alacorn_session_id=alacorn_id
        )
        return selected_track, note

    try:
        selected_track, result = await asyncio.to_thread(execute_note_post)
        
        if not selected_track:
            await update.message.reply_text(result)
            return

        # Handle object or dict response for track metadata
        if hasattr(selected_track, 'title'):
            track_title = selected_track.title
            artist_name = getattr(selected_track, 'display_artist', getattr(selected_track, 'artist_name', 'Artist'))
        else:
            track_title = selected_track.get("title", "Unknown Track")
            artist_name = selected_track.get("display_artist", "Unknown Artist")

        await update.message.reply_text(
            f"Successfully posted Music Note!\n\n"
            f"🎵 Song: {track_title} - {artist_name}\n"
            f"✍️ Caption: {note_caption}"
        )
    except Exception as e:
        logging.error(f"Error: {e}")
        await update.message.reply_text(f"Error posting note: {str(e)}")

if __name__ == "__main__":
    app = (
        ApplicationBuilder()
        .token(TELEGRAM_BOT_TOKEN)
        .connect_timeout(30.0)
        .read_timeout(30.0)
        .write_timeout(30.0)
        .pool_timeout(30.0)
        .build()
    )
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("note", post_music_note))

    print("Bot is running...")
    app.run_polling()

