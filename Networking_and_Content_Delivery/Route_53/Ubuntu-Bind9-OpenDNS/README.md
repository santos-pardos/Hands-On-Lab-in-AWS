## Configura Bind9

```
sudo apt update
sudo apt install -y bind9
sudo systemctl status named
sudo ufw allow bind9

sudo cat /etc/bind/named.conf.options


        forwarders {
                208.67.222.123;
         };
        
         allow-query { any; };

named-checkconf
sudo systemctl reload named
nslookup google.com localhost
nslookup google.com 172.31.20.77
sudo nano /etc/bind/db.red.lan

$TTL 1D
@ IN SOA ns.red.lan. instalador.red.lan. (
        1 ; serial
        604800 ; refresh
        86400 ; retry
        2419200 ; expiration
        604800 ; TTL negative cache
)
; Registros NS (Servidores de nombres)
@ IN NS ns.red.lan.
; Registros A
ns      IN      A 172.31.20.77
router  IN      A 172.31.20.1
pi      IN      A 172.31.20.11
puesto1 IN      A 172.31.20.100
puesto2 IN      A 172.31.20.101


named-checkzone red.lan /etc/bind/db.red.lan
sudo nano /etc/bind/named.conf.local

zone "red.lan" IN {
        type master;
        file "/etc/bind/db.red.lan";
};
sudo systemctl reload named
 nslookup puesto1.red.lan 172.31.20.77

sudo nano /etc/bind/db.0.31.172

$TTL 1D
@ IN SOA red.lan. root.red.lan. (
        0 ; serial
        604800 ; refresh
        86400 ; retry
        2419200 ; expires
        604800 ; TTL negative cache
)
@ IN NS ns.red.lan.
; Registros PTR
143     IN      PTR ns.red.lan.
1       IN      PTR router.red.lan.
130     IN      PTR pi.red.lan.
151     IN      PTR puesto1.red.lan.
152     IN      PTR puesto2.red.lan.

nnamed-checkzone 1.168.192 /etc/bind/db.0.31.172
sudo nano /etc/bind/named.conf.local

zone "1.168.192.in-addr.arpa" {
        type master;
        file "/etc/bind/db.1.168.192";
};

named-checkconf
sudo systemctl reload named
nslookup 172.31.20.1 172.31.20.77
```

## Links
https://comoinstalar.me/como-instalar-el-servidor-dns-bind-en-ubuntu-22-04-lts/?authuser=1
https://www.webhi.com/how-to/how-to-setup-and-configure-bind-as-a-private-network-dns-server/?authuser=1