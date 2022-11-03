#!/usr/bin/env python3

player = "Geoffrey Boycott"
total_matches = 609
batted = 1014
not_out = 162
total_run_scored = 48426

print('palyer:', player, sep=" ")
print('played in ' + str(total_matches) + " Matches")
print(f'scoring an average of {total_run_scored/(batted-not_out):.2f}')