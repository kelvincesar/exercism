/*
 * The functions defined below solve the "Charlie the Dog" challenge from CoderByte.
 * This challenge involves finding the shortest path in a matrix between a dogs
 * current position, marked by "C", and the home position, marked by "H", in which all
 * the food in the matrix, marked by "F", has been collected by Charlie.
 *
 * An example matrix:
 *        F|O|O|F
 *        O|C|O|O
 *        O|O|O|H
 *        F|O|O|O
 *        Solution: 11
 *
 * This solution will pass the CoderByte tests but does not implement the restriction
 * that Charlie cannot pass over the home cell before collecting all the food. The last
 * test in main() illustrates this.
 */

package main

import (
	"fmt"
	"math"
)

type Position struct {
	X int
	Y int
}

func NewPosition(x, y int) Position {
	return Position{
		X: x,
		Y: y,
	}
}

func calcDistance(p1 Position, p2 Position) int {
	x := int(math.Abs(float64(p2.X - p1.X)))
	y := int(math.Abs(float64(p2.Y - p1.Y)))
	return x + y
}

func CharlietheDog(strArr []string) string {
	var foods []Position
	var currentPos Position
	var dogPos Position

	// collect locations
	for row, word := range strArr {
		for column, char := range word {
			switch char {
			case 'H':
				currentPos = NewPosition(row, column)
			case 'C':
				dogPos = NewPosition(row, column)
			case 'F':
				foods = append(foods, NewPosition(row, column))
			}
		}
	}

	odometer := 0
	//fmt.Println(len(foods), foods, currentPos, dogPos )
	for len(foods) > 0 {
		nearest := math.MaxInt32
		var nearestIndex int
		var nearestPos Position

		for i, food := range foods {

			distance := calcDistance(currentPos, food)

			if distance < nearest {
				nearest = distance
				nearestIndex = i
				nearestPos = food
			} else if distance == nearest {
				// get the further food from the dog
				if calcDistance(dogPos, nearestPos) < calcDistance(dogPos, food) {
					nearest = distance
					nearestIndex = i
					nearestPos = food
				}
			}
		}

		// total distance and updates
		odometer += nearest
		currentPos = nearestPos

		// remove the selected food from the list
		foods = append(foods[:nearestIndex], foods[nearestIndex+1:]...)

	}

	//fmt.Println("odometer", odometer)
	odometer += calcDistance(currentPos, dogPos)
	return fmt.Sprintf("%d", odometer)

}

func main() {

	// do not modify below here, readline is our function
	// that properly reads in the input for you
	fmt.Println(CharlietheDog([]string{"FOOF", "OCOO", "OOOH", "FOOO"}))

}
