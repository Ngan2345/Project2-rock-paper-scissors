# Rock Paper Scissors

This is **Project 2** from **Udacity's Intro to Programming Nanodegree Program**.

## 1. Description
In this project, I was provided with the [starter code](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/November/5c002226_rps-starter-code/rps-starter-code.py) to further develop a computer version of the Rock Paper Scissors game.  
For each game, the human player will play against the computer for 3 rounds, after each of which the winner is announced.  
Besides, the final winner will also be decided according to the total score.


## 2. Language
- Python  

## 3. How to explore the data with the code

- Input `python starter.py` on your terminal to run this program
- Follow the instruction by typing `rock`, `paper` or `scissors` (case-insensitive) for each round of the game.  

## 4. More to note
- The computer player is designed to be on one of the following mode: 
  - `Player` who always plays `rock`
  - `CyclePlayer` who cycles through different moves after each round (`rock`, `paper` then `scissors`)
  - `RandomPlayer` who always chooses moves randomly
  - `ReflectPlayer` who plays what the human player plays in the previous round
- My starter.py code sets the computer player to be `CyclePlayer`, but you can change it by replacing `CyclePlayer()` with any other mode in line `123`.
- Perhaps, the most interesting way to play is to choose `RandomPlayer`, but feel free to try the other modes too to see how it turns out.