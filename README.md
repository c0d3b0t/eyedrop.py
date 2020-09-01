# eyedrop.py
Are you not curios about Linux desktop notifications? It's powered by Libnotify package. 

The best method to see how it works - it's to write a little script just like I did. It notifies me about my eye drops - 6 times each 10 minutes during 1 hour.

The script uses the `notify-send` command to send notifications. You will probably have it preinstalled in your system, like in the Linux Mint that I'm using. Otherwise the `apt-get install libnotify-bin` command will install it for you.

## Run the script

I was able to use both python2 and python3 to run this script, so the `python eyedrop.py` command should get it up and running.

Make an `eyedrop` command available globally:
- rename the "eyedrop.py" to eyedrop - `mv eyedrop.py eyedrop`
- make the file to be executable - `chmod +x eyedrop`
- move the file to `/usr/bin` directory - `mv eyedrop /usr/local/bin` (run with `sudo` if you aren't a root user).
