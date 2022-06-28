#!/bin/bash
#OUTPUT_FOLDER=/home/pi/Bierrallye/ZMS_python/out
#rm -r -f $OUTPUT_FOLDER
#mkdir $OUTPUT_FOLDER
#:>$OUTPUT_FOLDER/log.txt
#echo "python /home/pi/Bierrallye/ZMS_python/mainapp.py" >> $OUTPUT_FOLDER/log.txt

#V01
python /home/pi/Bierrallye/ZMS_python/mainapp.py #| tee -a $OUTPUT_FOLDER/log.txt #>> $OUTPUT_FOLDER/log.txt #2>> $OUTPUT_FOLDER/log.txt
#V02
#xterm -e python /home/pi/Bierrallye/ZMS_python/TwoRC522_RPi2-3/1-TwoRC522_RPi2-3/run_main_test.py &
#xterm -e python /home/pi/Bierrallye/ZMS_python/TwoRC522_RPi2-3/2-TwoRC522_RPi2-3/run_main_test.py &
