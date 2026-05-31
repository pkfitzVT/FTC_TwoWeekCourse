package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.hardware.DcMotor;

@TeleOp(name = "Demo Drive DPad", group = "YES Robotics")
public class DemoDriveDPad extends LinearOpMode {

    private DcMotor leftDrive;
    private DcMotor rightDrive;

    // Start with a moderate power so first tests are easier to control.
    private static final double DRIVE_POWER = 0.5;

    @Override
    public void runOpMode() {

        // These names must match the Robot Controller configuration exactly.
        leftDrive = hardwareMap.get(DcMotor.class, "leftDrive");
        rightDrive = hardwareMap.get(DcMotor.class, "rightDrive");

        telemetry.addLine("Demo Drive DPad Ready");
        telemetry.addLine("D-pad up: drive forward");
        telemetry.addLine("D-pad down: drive backward");
        telemetry.addLine("Left bumper: turn left");
        telemetry.addLine("Right bumper: turn right");
        telemetry.addLine("Release controls: stop");
        telemetry.update();

        waitForStart();

        while (opModeIsActive()) {

            // The main loop is readable because each movement is named.
            if (gamepad1.dpad_up) {
                driveForward(DRIVE_POWER);
                telemetry.addLine("Driving forward");
            } else if (gamepad1.dpad_down) {
                driveBackward(DRIVE_POWER);
                telemetry.addLine("Driving backward");
            } else if (gamepad1.left_bumper) {
                turnLeft(DRIVE_POWER);
                telemetry.addLine("Turning left");
            } else if (gamepad1.right_bumper) {
                turnRight(DRIVE_POWER);
                telemetry.addLine("Turning right");
            } else {
                allStop();
                telemetry.addLine("Stopped");
            }

            telemetry.addData("Drive power", DRIVE_POWER);
            telemetry.update();
        }
    }

    public void driveForward(double power) {
        leftDrive.setPower(-power);
        rightDrive.setPower(power);
    }

    public void driveBackward(double power) {
        leftDrive.setPower(power);
        rightDrive.setPower(-power);
    }

    public void turnLeft(double power) {
        leftDrive.setPower(power);
        rightDrive.setPower(power);
    }

    public void turnRight(double power) {
        leftDrive.setPower(-power);
        rightDrive.setPower(-power);
    }

    public void allStop() {
        leftDrive.setPower(0.0);
        rightDrive.setPower(0.0);
    }
}
