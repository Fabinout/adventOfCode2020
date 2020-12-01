static INPUT: &str = include_str!("../inputs/1.txt");

use itertools::Itertools as _;

fn find_summands(n: usize) -> Option<Vec<u32>> {
    INPUT
        .lines()
        .map(|x| x.parse::<u32>().unwrap())
        .combinations(n)
        .find(|x| x.iter().sum::<u32>() == 2020)
}

fn solve(n: usize) -> Option<u32> {
    find_summands(n).map(|x| x.iter().product())
}

fn main() {
    for x in &[2, 3] {
        println!("{}", solve(*x).unwrap());
    }
}
