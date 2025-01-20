import os
import subprocess

# Define a constant directory for all operations
BASE_DIR = r"D:\drm trying"
os.makedirs(BASE_DIR, exist_ok=True)  # Ensure the directory exists

def get_user_input():
    """Prompt the user for MPD URL and decryption key."""
    mpd_url = input("Enter the MPD URL: ").strip()
    decryption_key = input("Enter the decryption key (format: KID:KEY): ").strip()
    return mpd_url, decryption_key

def list_and_select_formats(mpd_url):
    """
    Use N_m3u8DL-RE to display all formats and allow the user to select desired ones interactively.
    """
    print("Displaying available video formats...")
    command = [
        "N_m3u8DL-RE",
        mpd_url,
    ]
    try:
        subprocess.run(command, check=True, cwd=BASE_DIR)  # Set working directory
        print("Use the interactive menu to select formats.")
    except subprocess.CalledProcessError as e:
        print(f"Error displaying formats: {e}")
        exit(1)

def download_selected_formats(mpd_url):
    """Download the selected video and audio formats using N_m3u8DL-RE."""
    print("Downloading selected video and audio formats...")
    command = [
        "N_m3u8DL-RE",
        mpd_url,
        "--save-dir", BASE_DIR,  # Ensure all files are saved to BASE_DIR
        "--auto-select",        # Automatically select the best tracks
        "--binary-merge",       # Merge segments into a single file
        "--external-downloader", "aria2c",  # Use aria2c for faster downloads
    ]
    try:
        subprocess.run(command, check=True, cwd=BASE_DIR)  # Set BASE_DIR as the working directory
        print("Download completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading files: {e}")
        exit(1)

def decrypt_files(decryption_key):
    """Prompt the user for video and audio file locations and decrypt them using mp4decrypt."""
    print("Decrypting video and audio files...")
    
    # Prompt the user for file locations
    video_file = input("Enter the full path of the encrypted video file: ").strip()
    audio_file = input("Enter the full path of the encrypted audio file: ").strip()

    decrypted_video = os.path.join(BASE_DIR, "decrypted_video.mp4")
    decrypted_audio = os.path.join(BASE_DIR, "decrypted_audio.m4a")

    # Decrypt video and audio files
    video_decrypt_command = [
        "mp4decrypt",
        "--key", decryption_key,
        video_file,
        decrypted_video
    ]
    audio_decrypt_command = [
        "mp4decrypt",
        "--key", decryption_key,
        audio_file,
        decrypted_audio
    ]

    try:
        subprocess.run(video_decrypt_command, check=True)
        subprocess.run(audio_decrypt_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error decrypting files: {e}")
        exit(1)

    print(f"Decryption completed. Files saved to {BASE_DIR}")
    return decrypted_video, decrypted_audio

def merge_to_mkv(decrypted_video, decrypted_audio, mpd_url):
    """Merge decrypted video and audio files into an MKV using mkvmerge."""
    print("Merging files into MKV...")
    output_name = os.path.basename(mpd_url).split(".")[0] + "_decrypted.mkv"
    output_file = os.path.join(BASE_DIR, output_name)

    merge_command = [
        "mkvmerge",
        "-o", output_file,
        decrypted_video,
        decrypted_audio
    ]
    try:
        subprocess.run(merge_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error merging files into MKV: {e}")
        exit(1)
    print(f"Files merged successfully into: {output_file}")

def main():
    # Step 1: Get inputs from the user
    mpd_url, decryption_key = get_user_input()

    # Step 2: Display available formats and allow selection
    list_and_select_formats(mpd_url)

    # Step 3: Download the selected formats
    download_selected_formats(mpd_url)

    # Step 4: Decrypt the downloaded files
    decrypted_video, decrypted_audio = decrypt_files(decryption_key)

    # Step 5: Merge the decrypted files into a single MKV
    merge_to_mkv(decrypted_video, decrypted_audio, mpd_url)

if __name__ == "__main__":
    main()
