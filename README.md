MonaServer Video Streaming System
=================================

This Python script allows you to set up a video streaming server using MonaServer and FFmpeg. It monitors live video streams published to the server and generates HLS (HTTP Live Streaming) playlists for each stream, making them accessible through a web interface.

Prerequisites
----------

Before you get started, ensure you have the following prerequisites:
- MonaServer installed on your system.
- FFmpeg installed on your system.
- Python 3.x installed on your system.

Installation
----------

1.Clone this repository to your local machine:

```bash

git clone https://github.com/yourusername/monaserver-streaming.git
```

2. Make sure you have MonaServer and FFmpeg installed on your system.

3. Install any required Python packages:

```bash
pip install -r requirements.txt
```

Usage
----------

1. Open a terminal window and navigate to the repository directory.

2. Run the script by executing:

```bash
python monaserver_streaming.py
```

The script will start MonaServer, monitor for live video streams, and convert them to HLS format. It also creates a web interface for viewing the streams.
Configuration

You can modify the script to suit your needs by changing the parameters and options in the following functions:
```
convert(name, folder): This function defines the FFmpeg command used to convert live streams to HLS format. You can customize the command according to your requirements.
checkStreams(): This function monitors the MonaServer logs for new streams. You can customize the logic for detecting and handling streams as needed.
```
Customizing the Web Interface

The script creates a basic web interface for viewing the streams. You can customize the web interface by modifying the HTML templates in the MonaServer_Win64/www directory.
Important 

Notes
----------

Make sure to have the necessary permissions and security measures in place for streaming and server access.
This script is designed for Windows environments, but you can modify it for other platforms as needed.
Ensure that you have proper firewall and network settings to allow the streaming server to function as expected.

License
----------

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
----------

This script relies on MonaServer and FFmpeg for streaming and video conversion.
Special thanks to the open-source community for their contributions.
Please feel free to contribute to this project and make it even better!
