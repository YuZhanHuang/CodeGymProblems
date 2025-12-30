# Meeting Rooms III

## Statement

You have an integer rooms, representing room numbers from 0 to rooms-1. Additionally, you are given a 2D integer array called meetings, where each element meetings[i] = [start_i, end_i] indicates that a meeting will be held in the half-closed interval [start_i, end_i). Each start_i is unique.

Meetings are allocated to rooms in the following manner:

- Each meeting will take place in the unused room with the lowest number.
- If there are no available rooms, the meeting will be delayed until a room becomes free, maintaining the same duration as the original meeting.
- When a room is vacated, the meeting with the earliest original start time is given priority for that room.

Your task is to determine the room number that hosted the highest number of meetings. If there are multiple rooms, return the room with the lowest number.

**Note:** A half-closed interval [a, b) is the interval between a and b including a and not including b.

## Constraints

- 1 ≤ rooms ≤ 100
- 1 ≤ meetings.length ≤ 10^4
- meetings[i].length == 2
- 0 ≤ start_i < end_i ≤ 5 × 10^5
- All start_i are unique.

