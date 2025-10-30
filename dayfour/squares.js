function isPerfectSquare(number) {
	if (number < 0) 
		return false;
	for (let check = 0; check <= number; check++) {
		if (check * check == number)
		return true;
			//check++;
        }
	return false;
    }
number = 4
console.log(isPerfectSquare(number))
    //let result = [];
    //for (let check = 0; check < number.length; check++) {
        //(isPerfectSquare[check]));
    //}
    //return result;
//}

