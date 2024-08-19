// Package weather will be used in the weather forecast.
package weather

// CurrentCondition is a global variable that will hold the current weather condition.
var CurrentCondition string
// CurrentLocation is a global variable that will hold the current location.
var CurrentLocation string

// Forecast returns the weather forecast for the given city and condition.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
