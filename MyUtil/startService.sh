#!/bin/bash


function startSP() {
	cd /fsp_sss_stream/apache-tomcat-sp/bin
	./shutdown.sh
	sleep 15s
	./startup.sh
	sleep 5s
}

function startAccess() {
	cd /fsp_sss_stream/apache-tomcat-access/bin/
	./shutdown.sh
	sleep 15s 
	./startup.sh
}

function startSC() {
	cd /fsp_sss_stream/sc/bin/
	./sc_stop.sh
	./sc_start.sh
}

function startGC() {
	cd /fsp_sss_stream/gc/bin/
	./sc_stop.sh
	./sc_start.sh
}

function startMS() {
	cd /fsp_sss_stream/ms/bin/
	./ms_stop.sh
	./ms_start.sh
}

function startMA() {
	cd /fsp_sss_stream/ma/bin/
	./ma_stop.sh
	./ma_start.sh
}

function startRule() {
	cd /fsp_sss_stream/rule/bin/
	./rule_stop.sh
	./rule_start.sh
}

function startGS() {
	cd /fsp_sss_stream/gs/
	nohup ./test_stream_server_ss < ss.config &

}

function startSS() {
	cd /fsp_sss_stream/ss/
	nohup ./test_stream_server_ss < ss.config &
}

function startCP() {
	cd /fsp_sss_stream/cp/
	nohup ./test_proxy < cp.config &
}

for service in "$@";do
	case "$service" in 
	access)
		startAccess
		;;
	sp)
		startSP
		;;
	sc)
		startSC
		;;
	gc)
		startGC
		;;
	ma)
		startMA
		;;
	ms)
		startMS
		;;
	rule)
		startRule
		;;
	gs)
		startGS
		;;
	ss)
		startSS
		;;
	cp)
		startCP
		;;
       	*)

		echo "invalid service: $service"
		exit 1
	esac
done


