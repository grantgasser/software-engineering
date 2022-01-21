/**
 * @param {string} s
 * @return {string}
 */
 var frequencySort = function(s) {
    // O(N)
    var freq = {};
    for (let ch of s) {
        freq[ch] = freq[ch] ? freq[ch] + 1 : 1;
    }
    
    // sort keys based on values, O(1)
    var sortedKeys = Object.keys(freq).sort((a, b) => {
       return freq[b] - freq[a]; 
    });
    
    // build result, O(1)
    var result = '';
    for (let ch of sortedKeys) {
        for (var i = 0; i < freq[ch]; i++) {
            result += ch;
        }
    }
    
    return result;
};