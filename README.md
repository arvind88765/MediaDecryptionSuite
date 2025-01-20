# 🎥 MediaDecryptionSuite

This Python script provides a comprehensive solution for handling video files, specifically focusing on downloading, decrypting, and merging video and audio streams from MPD (MPEG-DASH) URLs. It automates the entire process from fetching media through decryption to final file merging.

---

## 📜 What is My Script?

The MediaDecryptionSuite is ideal for users needing to manage encrypted video content, allowing them to easily decrypt and merge video and audio files into a single MKV file. It's particularly useful for educators, content creators, and developers working with digital media processing and distribution.

---

## 🚀 Use of the Script

Before you run the script, ensure you have the necessary tools installed:
- Python 3.x
- `N_m3u8DL-RE` CLI tool
- `mp4decrypt` from Bento4 tools
- `mkvmerge` from MKVToolNix
- `aria2c` for faster downloads

---

## 🔑 Requirements

You will need:
- The MPD URL of the video file you want to process.
- A decryption key in the format KID:KEY.

---

## ⚙️ Configuring the Script

Before running the script, you'll need to adjust the paths to the external tools used by the script according to their installation locations on your system. Here’s what you need to do:

1. **N_m3u8DL-RE Path**: Ensure that the `N_m3u8DL-RE` executable is in your system's PATH or modify the script to include the full path to the executable.
2. **mp4decrypt and mkvmerge**: Check that `mp4decrypt` and `mkvmerge` from Bento4 tools and MKVToolNix respectively, are accessible from your system's PATH. If not, provide the full path in the script where these commands are called.
3. **aria2c Path**: If you are using `aria2c` for faster downloads, ensure that its path is correctly set in the script or included in your system's PATH.
4. **Base Directory**: The `BASE_DIR` constant in the script is set to `"D:\drm trying"`. You should change this to a preferred directory on your system where you want the script to download and save files.

---

## 📌 Step-by-Step Guide

1. **Clone the Repository**:
   - Open your terminal.
   - Run the command `git clone https://github.com/arvind88765/MediaDecryptionSuite.git`.
2. **Change Directory**:
   - Change to the directory containing the script by running `cd MediaDecryptionSuite`.
3. **Install Dependencies**:
   - Make sure all required tools are installed on your system.
4. **Prepare Environment**:
   - Set the `BASE_DIR` in the script to a directory where you want the downloads and outputs to be saved.
5. **Run the Script**:
   - Run the script using the command `python drm.py`.
   - Follow the on-screen prompts to input the MPD URL and decryption key.
6. **Select Formats**:
   - Use the interactive menu provided by `N_m3u8DL-RE` to select the desired video and audio formats.
7. **Download and Decrypt**:
   - The script will handle the downloading and decryption of selected formats.
8. **Merge Files**:
   - Finally, decrypted video and audio files will be merged into an MKV file.

---

## 📚 Educational Purpose

This project is developed for educational purposes only. It is designed to demonstrate how to handle media files through processes such as downloading, decrypting, and merging. Please ensure that you have the legal right to access and manipulate any media files you work with using this toolkit.

## ⚠️ Disclaimer

The author of this repository is not responsible for any misuse of this software. Users are responsible for ensuring their actions comply with applicable laws and terms of service. Please use this script responsibly.

---

## 🌟 Support the Project

If you find this toolkit helpful, please consider giving it a ⭐️ on GitHub to show your support! Also, feel free to fork this repository to make your own modifications and share it with the community.

To star the project, click on the "Star" button at the top of this GitHub page. To fork, click on the "Fork" button alongside it. Your support helps keep the project alive and is greatly appreciated!

---

Thank you for checking out the MediaDecryptionSuite!
