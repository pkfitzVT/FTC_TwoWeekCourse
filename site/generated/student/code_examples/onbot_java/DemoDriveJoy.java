package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.eventloop.opmode.TeleOp;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.util.Range;

@TeleOp(name = "Demo Drive Joy", group = "YES Robotics")
public class DemoDriveJoy extends LinearOpMode {

    private DcMotor leftDrive;
    private DcMotor rightDrive;

    @Override
    public void runOpMode() {

        // These names must match the Robot Controller configuration exactly.
        leftDrive = hardwareMap.get(DcMotor.class, "leftDrive");
        rightDrive = hardwareMap.get(DcMotor.class, "rightDrive");

        telemetry.addLine("Demo Drive Joy Ready");
        telemetry.addLine("Left stick Y: forward/back");
        telemetry.addLine("Right stick X: turn");
        telemetry.addLine("Release sticks: stop");
        telemetry.update();

        waitForStart();

        while (opModeIsActive()) {

            // FTC joystick Y is negative when pushed forward, so the minus sign
            // makes pushing forward produce a positive drive value.
            double drive = -gamepad1.left_stick_y;
            double turn = gamepad1.right_stick_x;

            // This is direct joystick math. Students will compare this with
            // the method-based D-pad file.
            double leftPower = Range.clip(drive + turn, -1.0, 1.0);
            double rightPower = Range.clip(drive - turn, -1.0, 1.0);

            leftDrive.setPower(-leftPower);
            rightDrive.setPower(rightPower);

            telemetry.addData("Drive", drive);
            telemetry.addData("Turn", turn);
            telemetry.addData("Left power", leftPower);
            telemetry.addData("Right power", rightPower);
            telemetry.update();
        }
    }
}
