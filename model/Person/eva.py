from .person import Person
from datetime import datetime, timedelta


# Homer is a naive implementation for working skeleton
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
            percentage = (datetime.now() - self.phase_start).total_seconds() / self.learn_time.total_seconds()
            if percentage >= 1:
                percentage = 0.99
            return percentage
        if self.state == 2:
            if (datetime.now() - self.distracting_start) < self.tolerated_distraction:
                percentage = (datetime.now() - self.phase_start).total_seconds() / self.learn_time.total_seconds()
                if percentage >= 1:
                    percentage = 0.99
                return - percentage
            else:
                return 2
        if self.state == 3:
            percentage = (datetime.now() - self.phase_start).total_seconds() / self.pause_time.total_seconds()
            if percentage >= 1:
                percentage = 1
            return 1 + percentage

    def is_learning(self):
        if self.state == 2:
            self.state = 1
            self.phase_start += datetime.now() - self.distracting_start
        elif self.state == 3:
            self.state = 1
            self.phase_start = datetime.now()

    def is_relaxing(self):
        if self.state == 1:
            if self.okay_to_continue_threshold <= self.should_learn() < 1:
                self.state = 3
                self.phase_start = datetime.now()
            else:
                self.state = 2
                self.distracting_start = datetime.now()

    def is_mad(self):
        if self.state == 2:
            self.state = 3
            self.phase_start = datetime.now()
        if self.state == 1 and self.okay_to_continue_threshold <= self.should_learn() < 1:
            self.phase_start += timedelta(0, 60)
        if self.state == 3 and 1 + self.okay_to_continue_threshold <= self.should_learn() <= 2:
            self.phase_start += timedelta(0, 60)

    def is_leaving(self):
        self.state = 0

    def is_back(self):
        self.state = 1

    def is_distracted(self):
        pass

    def is_concentrated(self):
        pass

    def is_happy(self):
        pass
