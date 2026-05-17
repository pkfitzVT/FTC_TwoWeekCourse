# Session 9 Reading: Flywheel Speed and Ball Compression

## How a Flywheel Shooter Works

A flywheel shooter uses a spinning wheel to transfer energy to a ball. The motor spins the wheel, the wheel grips the ball, and the ball leaves the shooter with speed.

The basic system chain is:

```text
motor power -> wheel speed -> ball compression/contact -> launch speed
```

If one part of this chain is weak or inconsistent, the shot will be weak or inconsistent too.

## Shooter Vocabulary

A **flywheel** is a wheel that spins quickly and stores motion. In a shooter, the flywheel touches the ball and helps launch it.

A **shooter** is the robot mechanism that launches a ball or game piece toward a target.

A **motor** turns electrical energy into spinning motion.

A **motor shaft** is the spinning metal part coming out of the motor. The shaft may spin a wheel directly or through another connector.

**Rotation** means spinning around a center point.

**Rotations per minute**, or **RPM**, means how many full turns something makes in one minute.

**Wheel speed** means how fast the flywheel is spinning.

**Surface speed** means how fast the outside edge of the wheel is moving. The ball touches this outside edge.

**Power** is the command sent to the motor controller. More power usually tries to make the motor spin harder or faster.

**Torque** is twisting force. If a motor has more torque, it can push harder against resistance, such as when the ball presses into the spinning wheel.

A **load** is something that makes the motor work harder. A ball pressing into the wheel is a load.

**Friction** is rubbing force between surfaces.

**Traction** is useful grip. A flywheel needs enough traction to push the ball instead of slipping.

**Compression** is how much the ball is squeezed between the flywheel and the wall, ramp, or hood of the shooter.

A **gap** is the space the ball passes through near the flywheel.

**Elasticity** is how well the ball returns to its shape after being squeezed.

**Stiffness** is how hard it is to squeeze something.

A **soft wheel** squishes more when it touches the ball.

A **hard wheel** keeps its shape more when it touches the ball.

**Recovery time** is how long the shooter takes to get back to speed after launching a ball.

**Consistency** means getting similar results again and again.

## Power Is Not the Same as Speed

Motors turn electrical energy into rotation. The motor spins a shaft. The shaft spins a wheel. The spinning wheel pushes on the ball.

In FTC Java, this code sends full power to the shooter motor:

```java
shooterMotor.setPower(1.0);
```

This tells the motor controller to send full power to the motor, but the motor still has physical limits.

Full power does not mean the motor can spin infinitely fast. Actual speed depends on the motor, battery voltage, friction, load, and the ball pressing into the wheel.

## Speed and Torque Are Different

Speed means how fast the motor spins. Torque means twisting force.

A motor spinning very fast usually has less extra torque available to push through resistance. When a ball presses into the wheel, the wheel may slow down for a moment.

A good shooter needs enough speed to launch the ball and enough torque to recover after each shot.

## Compression Matters

Compression is how much the ball is squeezed between the wheel and the wall or ramp of the shooter.

Too little compression can cause slipping. The wheel spins, but it does not push the ball strongly.

Too much compression can jam the ball, slow the motor, or make shots inconsistent.

Wheel firmness and gap size work together. Softer wheels may grip more and squish more. Harder wheels may keep their shape better but may slip more.

The best gap depends on the ball size, wheel firmness, ball elasticity, and wheel speed. There is no magic number until your team tests with your parts.

## Design Choices

| Design Choice | Possible Benefit | Possible Problem |
|---|---|---|
| More compression | More grip on the ball | More motor slowdown or jamming |
| Less compression | Less motor slowdown | Ball may slip or launch weakly |
| Softer wheel | Better grip and contact | May absorb energy or deform too much |
| Harder wheel | Holds shape well | May slip if contact is poor |
| Higher motor power | More possible launch speed | More bounce, more variation, more battery drain |

## Reflection

Why is the fastest possible wheel speed not always the best shooter design?

What compression gap does your team want to test first, and why?
