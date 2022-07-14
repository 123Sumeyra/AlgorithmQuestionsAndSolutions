package com.sum.algorima


fun main() {

    val result =   compareArray(arrayOf(5, 6, 3, 8), arrayOf(1, 3, 4,9))

    println(result.joinToString(" ")) // 2,2


}


fun compareArray(a: Array<Int>, b: Array<Int>): Array<Int> {

    var aPoint = 0
    var bPoint = 0

    for (index in a.indices) { // i in 0..arrayname.size-1
        when {
            a[index] > b[index] -> aPoint += 1

            b[index] > a[index] ->  bPoint += 1

        }
    }

    return arrayOf(aPoint, bPoint)
}