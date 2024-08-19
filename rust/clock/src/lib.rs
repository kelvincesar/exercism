use std::fmt;

const MINUTES_IN_A_DAY: i32 = 60*24;

#[derive(Debug)]
pub struct Clock {
    hours: i32,
    minutes: i32
}

impl Clock {
    pub fn new(hours: i32, minutes: i32) -> Self {
       
        let total_minutes = Clock::to_minutes(hours, minutes);

        let hours = (total_minutes / 60) % 24;
        let minutes = total_minutes % 60;

        Self { hours, minutes }
    }

    pub fn add_minutes(&self, minutes: i32) -> Self {
        Clock::new(self.hours, self.minutes + minutes)
    }

    fn to_minutes(hours: i32, minutes: i32) -> i32 {
        let total = (hours * 60 + minutes) % MINUTES_IN_A_DAY;
        if total < 0 {
            return total + MINUTES_IN_A_DAY;
        }

        total
    }

}

impl fmt::Display for Clock {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:02}:{:02}", self.hours, self.minutes)
    }
}

impl PartialEq for Clock {
    fn eq(&self, other: &Self) -> bool {
        (self.hours == other.hours) && (self.minutes == other.minutes)
    }
}

impl Eq for Clock {}