from .person import Person
from datetime import datetime, timedelta


# Calculate which portion of a time frame is already over
def portion(time, max_time, max_value):
    res = 0.01 + (datetime.now() - time).total_seconds() / max_time.total_seconds()
    if res >= 1:
        return max_value
    return res


# Eva is an implementation based on the first user study
class Eva(Person):
    state = 0  # 0:off 1:active_learning 2:distracted_learning 3:pause
    phase_start = datetime.now()
    distracting_start = datetime.now()

    okay_to_continue_threshold = 0.8  # After which should_learn values (x and 1+x) is a switch to the other phase accepted
    learn_time = timedelta(0, 180)  # How long should be learned
    pause_time = timedelta(0, 60)  # How long should be relaxed
    tolerated_distraction = timedelta(0, 10)  # How long should a distraction be tolerated

    def should_learn(self):
        # 0:        model paused        negative:   yellow
        # ]0,1[:    learning            after 0.8:  blink
        # [1,2[:    pause
        # 2:        alarm
        if self.state == 0:
            return 0
        if self.state == 1:
            percentage = portion(self.phase_start, self.learn_time, 2)
            return round(percentage, 2)
        if self.state == 2:
            if (datetime.now() - self.distracting_start) < self.tolerated_distraction:
                real_phase_start = self.phase_start + (datetime.now() - self.distracting_start)
                percentage = portion(real_phase_start, self.learn_time, 0.99)
                return round(- percentage, 2)
            else:
                return 2
        if self.state == 3:
            percentage = portion(self.phase_start, self.pause_time, 1)
            return round(1 + percentage, 2)

    def is_learning(self):
        if self.state == 2:
            self.state = 1
            self.phase_start += datetime.now() - self.distracting_start
        elif self.state == 3:
            self.state = 1
            self.phase_start = datetime.now()

    def is_relaxing(self):
        if self.state == 1:
            if self.okay_to_continue_threshold <= self.should_learn():
                self.state = 3
                self.phase_start = datetime.now()
            else:
                self.state = 2
                self.distracting_start = datetime.now()

    def is_mad(self):
        if self.state == 2 and self.should_learn() == 2:
            self.state = 3
            self.phase_start = datetime.now()
        if self.state == 1 and self.okay_to_continue_threshold <= self.should_learn():
            self.phase_start += timedelta(0, 60)
        if self.state == 3 and 1 + self.okay_to_continue_threshold <= self.should_learn():
            self.phase_start += timedelta(0, 30)

    def is_leaving(self):
        self.state = 0

    def is_back(self):
        if self.state == 0:
            self.state = 1
            self.phase_start = datetime.now()

    def is_distracted(self):
        pass

    def is_concentrated(self):
        pass

    def is_happy(self):
        pass
