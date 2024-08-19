use std::fmt::Debug;
use std::cmp::Ordering;

#[derive(Debug, PartialEq, Eq)]
pub enum Comparison {
    Equal,
    Sublist,
    Superlist,
    Unequal,
}

pub fn sublist<T: PartialEq + Debug>(first_list: &[T], second_list: &[T]) -> Comparison {
    if first_list.len().eq(&0) && second_list.len().gt(&0) {
        return Comparison::Sublist;
    }
        
    if second_list.len().eq(&0) && first_list.len().gt(&0) {
        return Comparison::Superlist;
    }

    match first_list.len().cmp(&second_list.len()) {
        Ordering::Equal if first_list == second_list => Comparison::Equal,
        Ordering::Greater => {
            if first_list.windows(second_list.len()).any(|window| window == second_list) {
                Comparison::Superlist
            } else {
                Comparison::Unequal
            }
        }
        Ordering::Less => {
            if second_list.windows(first_list.len()).any(|window| window == first_list) {
                Comparison::Sublist
            } else {
                Comparison::Unequal
            }
        },
        _=> Comparison::Unequal
    }
}