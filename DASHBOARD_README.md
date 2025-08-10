# MHDDoS Web Dashboard

A modern web-based dashboard for controlling MHDDoS attacks with a beautiful dark-themed interface.

## Features

- 🌐 **Web-based Interface**: Access from any device with a web browser
- 🎨 **Modern Dark Theme**: Beautiful UI matching the stress panel design
- ⚡ **Real-time Monitoring**: Live updates of running attacks
- 🎯 **All Attack Methods**: Support for all Layer 4 and Layer 7 methods
- 📊 **Attack Management**: Start, stop, and monitor multiple attacks
- 📱 **Responsive Design**: Works on desktop and mobile devices

## Quick Start

### Method 1: Using the startup script (Recommended)
```bash
python3 run_dashboard.py
```

### Method 2: Manual installation
```bash
# Install dependencies
pip install -r requirements_dashboard.txt

# Start the dashboard
python3 app.py
```

### Method 3: Direct Flask run
```bash
# Install Flask and psutil
pip install Flask psutil

# Run the application
python3 app.py
```

## Accessing the Dashboard

1. Start the dashboard using any of the methods above
2. Open your web browser
3. Navigate to: `http://localhost:5000`
4. The dashboard will load with the stress panel interface

## Dashboard Features

### Attack Configuration
- **Layer 4 Attacks**: TCP, UDP, SYN, VSE, TS3, MCPE, FIVEM, MINECRAFT, CPS, CONNECTION, MCBOT, ICMP, MEM, NTP, DNS, ARD, CLDAP, CHAR, RDP
- **Layer 7 Attacks**: CFB, BYPASS, GET, POST, OVH, STRESS, DYN, SLOW, HEAD, NULL, COOKIE, PPS, EVEN, GSB, DGB, AVB, CFBUAM, APACHE, XMLRPC, BOT, BOMB, DOWNLOADER, KILLER, TOR, RHEX, STOMP
- **Telegram Attacks**: Placeholder for future Telegram session attacks

### Attack Parameters
- **Host**: Target IP address or domain
- **Port**: Target port (default: 80)
- **Time**: Attack duration in seconds
- **Method**: Select from available attack methods
- **Concurrents**: Number of concurrent threads
- **RPC**: Requests per connection (Layer 7 only)
- **Proxy Type**: HTTP, SOCKS4, SOCKS5, or All (Layer 7 only)

### Attack Management
- **Real-time Status**: Monitor running attacks
- **Stop Individual**: Stop specific attacks
- **Stop All**: Stop all running attacks
- **Attack History**: View completed and stopped attacks

## File Structure

```
MHDDoS-main/
├── app.py                    # Flask application
├── run_dashboard.py          # Startup script
├── requirements_dashboard.txt # Dashboard dependencies
├── templates/
│   └── dashboard.html        # Dashboard interface
├── start.py                  # Original MHDDoS script
├── config.json              # MHDDoS configuration
└── files/                   # MHDDoS files directory
```

## Requirements

- Python 3.7+
- Flask 2.3.3+
- psutil 5.9.5+
- All original MHDDoS dependencies

## Security Notes

⚠️ **Important**: This dashboard provides web access to DDoS tools. Use responsibly and only on systems you own or have permission to test.

- The dashboard runs on `0.0.0.0:5000` by default (accessible from any IP)
- Consider using a firewall or VPN for additional security
- Change default settings for production use

## Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in `app.py` or kill the process using port 5000
2. **Missing dependencies**: Run `pip install -r requirements_dashboard.txt`
3. **start.py not found**: Make sure you're in the MHDDoS directory
4. **Permission denied**: Run with appropriate permissions for your system

### Error Messages

- **"Method Not Found"**: The selected method doesn't exist in MHDDoS
- **"Cannot resolve hostname"**: Check the target URL/IP address
- **"Proxy Check failed"**: Network or proxy configuration issue

## Support

For issues related to:
- **Dashboard**: Check this README and the Flask logs
- **MHDDoS**: Refer to the original MHDDoS documentation
- **Dependencies**: Ensure all requirements are properly installed

## License

This dashboard is provided as-is for educational and testing purposes. Use responsibly and in accordance with applicable laws and regulations.
