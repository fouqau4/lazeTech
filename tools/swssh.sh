#!/bin/bash

devices=(\
#"example"\
)
user=(\
#"username"\
)
ip=(\
#"1.2.3.4"\
)
port=(\
#9527\
)

ssh_login(){
	idx=$1
	user=${user[$idx]}
	ip=${ip[$idx]}
	port=${port[$idx]}

	tmux new -s ${devices[$idx]} ssh $user@$ip -p $port
}

target=$1

if [ "$#" -eq 0 ]; then
	echo -e "Select the device:"
	for idx in ${!devices[*]}
	do
		echo -e "  [$idx]: ${devices[$idx]}"
	done

	read target
fi

ssh_login $target
