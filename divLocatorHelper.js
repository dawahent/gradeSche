//Two main functionality in this script
//looking for the top parent (semesterCard) of an element
//looking for specific element of a semesterCard

function locateParentId(ele,searchId){
  if(ele.id === searchId)
    return ele;
  return locateParentId(ele.parentNode,searchId);
}

//the two functions below assume the first input cardEle is an element
function scanForId(cardEle,searchId){
  if(cardEle.childNodes.length === 0) return null;
  if(cardEle.id === searchId) return cardEle;
  for(let i = 0; i < cardEle.childNodes.length; i++){
    let temp = scanForId(cardEle.childNodes[i], searchId);
    if(!!temp)
      return temp;
  }
  return null;
}

function scanForLastId(cardEle, searchId){
  let toRet = null;

  if(cardEle.id === searchId) toRet = cardEle;
  if(cardEle.childNodes.length === 0) return toRet;

  for(let i = 0; i < cardEle.childNodes.length; i++){
    let temp = scanForId(cardEle.childNodes[i], searchId);
    if(!!temp)
      toRet = temp;
  }
  return toRet;
}

function scanForIdAll_helper(ele, searchId, arrayToRet){
  if(ele.id === searchId) arrayToRet.push(ele);
  if(ele.childNodes.length === 0) return;
  for (let i = 0; i < ele.childNodes.length; i++){
    scanForIdAll_helper(ele.childNodes[i], searchId, arrayToRet);
  }
}

function scanForIdAll(cardEle, searchId){
  let toRet = [];
  scanForIdAll_helper(cardEle, searchId, toRet);
  return toRet;
}
