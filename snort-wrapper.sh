#!/bin/sh
# Source function library.
. /etc/rc.d/init.d/functions

# Source the local configuration file
. /etc/sysconfig/snort

# Convert the /etc/sysconfig/snort settings to something snort can
# use on the startup line.
if [ "$ALERTMODE"X = "X" ]; then
   ALERTMODE=""
else
   ALERTMODE="-A $ALERTMODE"
fi

if [ "$USER"X = "X" ]; then
   USER="snort"
fi

if [ "$GROUP"X = "X" ]; then
   GROUP="snort"
fi

if [ "$BINARY_LOG"X = "1X" ]; then
   BINARY_LOG="-b"
else
   BINARY_LOG=""
fi

if [ "$CONF"X = "X" ]; then
   CONF="-c /etc/snort/snort.conf"
else
   CONF="-c $CONF"
fi

if [ "$INTERFACE"X = "X" ]; then
   INTERFACE="-i eth0"
else 
   INTERFACE="-i $INTERFACE"
fi

if [ "$DUMP_APP"X = "1X" ]; then
   DUMP_APP="-d"
else
   DUMP_APP=""
fi 

if [ "$NO_PACKET_LOG"X = "1X" ]; then
   NO_PACKET_LOG="-N"
else
   NO_PACKET_LOG=""
fi      

if [ "$PRINT_INTERFACE"X = "1X" ]; then
   PRINT_INTERFACE="-I"
else
   PRINT_INTERFACE=""
fi

if [ "$PASS_FIRST"X = "1X" ]; then
   PASS_FIRST="-o"
else
   PASS_FIRST=""
fi

if [ "$LOGDIR"X = "X" ]; then
   LOGDIR=/var/log/snort
fi

RETVAL=0

chown -R snort:snort $LOGDIR
/usr/sbin/snort -c /etc/snort/snort.conf -T > /dev/null 2>&1
RETVAL=$?
if [ "$RETVAL" != "0" ]; then
        failure
        echo
        exit $RETVAL
fi
cd $LOGDIR
if [ "$INTERFACE" = "-i ALL" ]; then
    for i in `cd /proc/sys/net/ipv4/conf; ls -d eth* |sed s/"\/"//g`
    do
        mkdir -p "$LOGDIR/$i"
        chown -R snort:snort $LOGDIR
        daemon /usr/sbin/snort $ALERTMODE $BINARY_LOG $NO_PACKET_LOG $DUMP_APP -D $PRINT_INTERFACE -i $i -u $USER -g $GROUP $CONF -l $LOGDIR/$i $PASS_FIRST
    done
else
    daemon /usr/sbin/snort $ALERTMODE $BINARY_LOG $NO_PACKET_LOG $DUMP_APP -D $PRINT_INTERFACE $INTERFACE -u $USER -g $GROUP $CONF -l $LOGDIR $PASS_FIRST
fi
touch /var/lock/subsys/snort
echo
