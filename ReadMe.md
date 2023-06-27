## Balus MyCobot

The primary purpose of the Balus Cobot is to support users in increasing learning effectiveness and
support users to adhere to more suitable learning and pause sequences.

### Model

The Different Persons in the [Person](./model/Person) folder represent the behaviors of user types.
In the final model, the following transitions are allowed:



### View

The [Cobot](./view/cobot.py) file is the main component used to pass instructions along to the actual MyCobot.
Effectively, the Cobot class takes the input provided through the url fed by Model and Controller and maps the received values to corresponding actions taken by the MyCobot.
The following mappings are provided:

| input_state | Cobot_Action | Color          |
|-------------|--------------|----------------|
| [0.0, 0.0]  | Hide         | Off            |
| (0.0, 0.8)  | Sleep        | Off (Yellow)   |
| [0.8, 1.0)  | Wake_Up      | Off - Green    |
| [1.0, 1.8)  | Wiggle       | Green (Yellow) |
| [1.8, 2.0)  | Fall_Asleep  | Green - Off    |
| [2.0, 2.0]  | Straight     | Red            |

### Controller

The Interactions and current state of the user are tracked through the [Webcam](./controller/webcam_activity.py) and the [Computer](./controller/computer_activity.py) respectively.
