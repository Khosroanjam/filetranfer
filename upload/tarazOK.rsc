# apr/04/2020 16:58:20 by RouterOS 6.45.8
# software id = T30D-IZ50
#
# model = 951G-2HnD
# serial number = 642E06894F85
/interface bridge
add arp=proxy-arp name=LAN
/interface wireless
set [ find default-name=wlan1 ] ssid=MikroTik
/interface ethernet
set [ find default-name=ether1 ] arp=proxy-arp comment=internet
/interface pppoe-client
add add-default-route=yes disabled=no interface=ether1 name=pppoe-out1 \
    password=55355228 use-peer-dns=yes user=fhmtde2314942@stct8
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/ip ipsec peer
# This entry is unreachable
add name=peer1 passive=yes send-initial-contact=no
/ip ipsec profile
set [ find default=yes ] dh-group=modp1024 enc-algorithm=aes-256,aes-128,3des \
    nat-traversal=no
/ip ipsec proposal
set [ find default=yes ] auth-algorithms=sha512,sha1 enc-algorithms=\
    aes-256-cbc,aes-128-cbc,3des
/ip pool
add name=dhcp_pool0 ranges=192.168.1.21-192.168.1.199
add name=l2tp ranges=192.168.1.5-192.168.1.20
/ip dhcp-server
add address-pool=dhcp_pool0 disabled=no interface=LAN name=dhcp1
/ppp profile
add change-tcp-mss=yes dns-server=8.8.8.8,4.2.2.4 local-address=192.168.1.1 \
    name=l2tp remote-address=l2tp use-compression=yes use-encryption=yes \
    use-upnp=yes
/interface bridge port
add bridge=LAN interface=ether2
add bridge=LAN interface=ether3
add bridge=LAN interface=ether4
add bridge=LAN interface=ether5
/interface l2tp-server server
set authentication=mschap2 default-profile=l2tp enabled=yes ipsec-secret=3545 \
    use-ipsec=yes
/interface pptp-server server
set authentication=pap,chap,mschap1,mschap2 default-profile=default enabled=\
    yes
/ip address
add address=192.168.1.1/24 interface=LAN network=192.168.1.0
/ip dhcp-server network
add address=192.168.1.0/24 gateway=192.168.1.1
/ip firewall filter
add chain=input comment=L2tp_IPSEC port=1701,500,4500 protocol=udp
add chain=input protocol=ipsec-esp
add chain=input protocol=ipsec-ah
/ip firewall nat
add action=masquerade chain=srcnat out-interface=pppoe-out1
add action=dst-nat chain=dstnat disabled=yes dst-address=5.238.52.161 \
    dst-port=5060 protocol=udp to-addresses=192.168.1.250 to-ports=5060
add action=dst-nat chain=dstnat disabled=yes dst-address=5.238.52.161 \
    dst-port=10000-20000 protocol=udp to-addresses=192.168.1.250 to-ports=\
    10000-20000
add action=dst-nat chain=dstnat dst-address=91.92.211.165 dst-port=80 \
    protocol=tcp to-addresses=192.168.1.120 to-ports=80
add action=dst-nat chain=dstnat dst-address=91.92.211.165 dst-port=8080 \
    protocol=tcp to-addresses=192.168.1.240 to-ports=80
add action=dst-nat chain=dstnat dst-address=91.92.211.165 dst-port=902 \
    protocol=tcp to-addresses=192.168.1.202 to-ports=902
add action=dst-nat chain=dstnat dst-address=91.92.211.165 dst-port=443 \
    protocol=tcp to-addresses=192.168.1.202 to-ports=443
add action=dst-nat chain=dstnat dst-address=91.92.211.165 dst-port=8081 \
    protocol=tcp to-addresses=192.168.1.250 to-ports=80
/ip firewall service-port
set sip disabled=yes
/ip ipsec identity
add generate-policy=port-strict peer=peer1 secret=3545
/ip ipsec policy
set 0 dst-address=0.0.0.0/0 src-address=0.0.0.0/0
/ip service
set telnet disabled=yes
set ftp disabled=yes
set www disabled=yes
set ssh disabled=yes
set api disabled=yes
set winbox port=3545
set api-ssl disabled=yes
/ppp secret
add name=enayati password=@123@abc profile=l2tp service=l2tp
add name=taraz301 password=T@raz301 profile=l2tp service=l2tp
add name=taraz319 password=T@raz319 profile=l2tp service=l2tp
add name=taraz311 password=T@raz311 profile=l2tp service=l2tp
add name=taraz315 password=T@raz315 profile=l2tp service=l2tp
add name=taraz305 password=T@raz305 profile=l2tp service=l2tp
add name=taraz307 password=T@raz307 profile=l2tp service=l2tp
add name=taraz317 password=T@raz317 profile=l2tp service=l2tp
/system clock
set time-zone-name=Asia/Tehran
