package com.sum.algoritma



fun  main(){
    println(sumArray(arrayListOf(1,2,3,4)))
}
fun sumArray(array: ArrayList<Int>):Int{
    var sum = 0

    for(i in array){
        sum += i
    }

    return sum

}