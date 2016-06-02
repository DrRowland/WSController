# WSController  
(Writen for [RetroPie](https://retropie.org.uk/download/) v3.8 for RPi2/3)

Setup notes (optional):

RPi3 as WiFi Access Point  
https://frillip.com/using-your-raspberry-pi-3-as-a-wifi-access-point-with-hostapd/

Port 8080 -> 80 (run server as user)
```
# iptables -A INPUT -i wlan0 -p tcp --dport 80 -j ACCEPT
# iptables -A INPUT -i wlan0 -p tcp --dport 8080 -j ACCEPT
# iptables -A PREROUTING -t nat -i wlan0 -p tcp --dport 80 -j REDIRECT --to-port 8080
# iptables-save > /etc/iptables.ipv4.nat
```
/etc/dnsmasq.conf
```
 + no-hosts
 + addn-hosts=/etc/hosts.dnsmasq
```
/etc/hosts.dnsmasq
```
 + 172.24.1.1 rpi
```
cron (systemd would be better)
```
@reboot /home/pi/runme.sh
```
