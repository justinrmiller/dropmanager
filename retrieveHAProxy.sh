echo "Grabbing dependencies: make gcc vim"
sudo apt-get -y install make gcc vim

cd /root
echo "Grabbing HAProxy"
wget http://haproxy.1wt.eu/download/1.4/src/haproxy-1.4.23.tar.gz
tar -zvxf haproxy-1.4.23.tar.gz
cd haproxy-1.4.23

echo "Making HAProxy"

make TARGET=linux26

echo "Copying HAProxy to /usr/sbin/haproxy"
cp haproxy /usr/sbin/haproxy

echo "Starting HAProxy"
haproxy -p /var/run/haproxy.pid -f /etc/haproxy.cfg &
