/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
  if (strs.length === 1) {
    return strs[0];
  }

  let commonPrefix = strs[0];

  for (let i = 1; i < strs.length; i++) {
    let curr = strs[i];
    let j = 0;

    // Compare only until the length of the shorter prefix
    while (j < commonPrefix.length && curr[j] === commonPrefix[j]) { 
      j++;
    }

    // Update the prefix
    commonPrefix = commonPrefix.substring(0, j); 
  }

  return commonPrefix;
};
