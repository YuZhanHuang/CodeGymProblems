# Reconstruct Itinerary

## Statement

Given a list of airline tickets where tickets[i] = [from_i, to_i] represent a departure airport and an arrival airport of a single flight, reconstruct the itinerary in the correct order and return it.

The person who owns these tickets always starts their journey from "JFK". Therefore, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should prioritize the one with the smallest lexical order when considering a single string.

For example, the itinerary ["JFK", "EDU"] has a smaller lexical order than ["JFK", "EDX"].

**Note**: You may assume all tickets form at least one valid itinerary. You must use all the tickets exactly once.

## Constraints

- 1 ≤ tickets.length ≤ 300
- tickets[i].length = 2
- from_i.length = 3
- to_i.length = 3
- from_i ≠ to_i
- from_i and to_i consist of uppercase English letters.

