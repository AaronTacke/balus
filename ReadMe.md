## Balus MyCobot

The primary purpose of the Balus Cobot is to support users in increasing learning effectiveness and
support users to adhere to more suitable concentration and pause sequences.

To be able to follow the "Nutzerzentrierter Designprozess" we decided on a model-view-controller architecture which allows rapid development in flexible iterations due to its separation of concerns.

### Model

The different user models in the [Person folder](./model/Person) represent the state of the current user allowing for giving learning advices.
To process the observations the roboter makes about his environment and the user, an abstract [Person class](./model/Person/person.py) must be inherited.

The following implementations were created in the different iterations of the project:
- [Homer](./model/Person/homer.py): A naive implementation for a working skeleton of the Model-View-Controller Architecture
- [Eva](./model/Person/eva.py): A fully functional implementation based on the insights gained during the first user study
- [Inken](./model/Person/inken.py): This model includes the optimizations discussed in the debriefing after the expert study

In the final model ([Inken](./model/Person/inken.py)), the following interactions (among other things) are supported:
- Cycling between studying and learning in an advisable rhythm without disturbing interruptions
- Checking the activity of the user when learning on his computer
- Warning the user if the end of a phase is advisable (can be postponed)
- Urging the user to pause when a break is long overdue (can be postponed)
- Exhorting the user to stop with unintended distractions during concentration phases (can be postponed)
- Convincing the user to learn when he is not responding at the end of a break (can be postponed)
- Deactivating at any point in time when the according gesture (thumbs down) is detected
- Activating the robot and continue learning where stopped previously (thumbs up)
- Postpone the current recommendation when recognising the stop-gesture

The webservice that orchestrates the controllers and views, and offers a clear overview of the API functionalities is managed by the [model.py](./model/model.py) script.

### View

The [Cobot](./view/cobot.py) file is the main component used to pass instructions along to the actual MyCobot.
Effectively, the Cobot class takes the input provided through the url fed by Model and Controller and maps the received values to corresponding actions taken by the MyCobot.
The following mappings are provided:

| input_state | Cobot_Action | Color           | Meaning                  | Korrekt Verstanden [n=10] |
|-------------|--------------|-----------------|--------------------------|---------------------------|
| [0.0, 0.0]  | Hide         | Off             | Robot is inactive        | 70%                       |
| (0.0, 0.8)  | Sleep        | Off (Yellow)*   | User learns              | 100%                      |
| [0.8, 1.0)  | Wake_Up      | Off -> Green    | User should take a break | 50%                       |
| [1.0, 1.8)  | Wiggle       | Green (Yellow)* | User takes a break       | 60%                       |
| [1.8, 2.0)  | Fall_Asleep  | Green -> Off    | User should learn        | 20%                       |
| [2.0, 2.0]  | Straight     | Red             | User must comply now     | 50%                       |

*) if the sign bit of the input_state is set, the alternative color is used as a warning sign.

If any other representations are desirable, please refer to the minimal [print.py](./view/print.py) example to access the suggestions of the model.

### Controller

The Interactions and current state of the user are tracked through the [Webcam](./controller/webcam_activity.py) and the [Computer](./controller/computer_activity.py) respectively.

The Webcam controller is used for recognising gestures (thumbs up, thumbs down, stop) while the Computer controller observes user input.
In our prototype, any computer input is counted as the user being concentrated.
