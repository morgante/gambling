// var os = require('os');

//the seed pair itself
var clientSeed = process.env.DICE_CLIENT_SEED; //dont forget to exclude the dash and the nonce!
var serverSeed = process.env.DICE_SERVER_SEED;

// hash: 63bd93d0a886a355d8c039dc60d8712b0e974107d6ba42e887fa3fd49eb713f1

//bet made with seed pair (excluding current bet)
var nonce      = 17;

//crypto lib for hmac function
var crypto = require('crypto');

var roll = function(key, text) {

    //create HMAC using server seed as key and client seed as message
    var hash = crypto.createHmac('sha512', key).update(text).digest('hex');

    var index = 0;

    var lucky = parseInt(hash.substring(index * 5, index * 5 + 5), 16);

    //keep grabbing characters from the hash while greater than 
    while (lucky >= Math.pow(10, 6)) {
        index++;
        lucky = parseInt(hash.substring(index * 5, index * 5 + 5), 16);

        //if we reach the end of the hash, just default to highest number
        if (index * 5 + 5 > 128) {
            lucky = 99.99;
            break;
        }
    }

    lucky %= Math.pow(10, 4);
    lucky /= Math.pow(10, 2);

    return lucky;
}
console.log(roll(serverSeed, clientSeed+'-'+nonce));