#!/usr/bin/bash

case ${1,,} in
	mateus |administrator)
		echo "Hello, you're the boss here"
		;;
	help)
		echo "Just enter your username!"
		;;
	*)
		echo "Hello there. You're not boss of me. Enter a valid username!"
esac	
