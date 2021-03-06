#pragma config(Motor,  port2,           fLeftMotor,    tmotorVex393_MC29, openLoop)
#pragma config(Motor,  port3,           bLeftMotor,    tmotorVex393_MC29, openLoop)
#pragma config(Motor,  port8,           bRightMotor,   tmotorVex393_MC29, openLoop)
#pragma config(Motor,  port9,           fRightMotor,   tmotorVex393_MC29, openLoop)
//*!!Code automatically generated by 'ROBOTC' configuration wizard               !!*//

task main()
{

	configureSerialPort(uartTwo,uartUserControl);
	setBaudRate(uartTwo,baudRate115200);

	while(1){
		//motor[bLeftMotor]=vexRT[Ch3];
		//motor[fLeftMotor]=vexRT[Ch3];
		//motor[bRightMotor]=vexRT[Ch2];
		//motor[fRightMotor]=vexRT[Ch2];
		int receive = getChar(uartTwo);

		if(receive != -1){
			writeDebugStreamLine("%d",receive);
			switch(receive) {
			case ((int)'q'):
				motor[bLeftMotor] = 30;
				break;
			case ((int)'w'):
				motor[fLeftMotor] = 30;
				break;
			case ((int)'e'):
				motor[bRightMotor] = 30;
				break;
			case ((int)'r'):
				motor[fRightMotor] = 30;
				break;
			case ((int)'x'):
				motor[fRightMotor] = 0;
				motor[bRightMotor] = 0;
				motor[fLeftMotor] = 0;
				motor[bLeftMotor] = 0;
				break;
		}
	}
		//TODO: better protocol (timeout, motor speed, etc)
		wait1Msec(30);
}

}
