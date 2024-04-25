// alert 메시지를 대체할 함수
window.alert = function(message) {
    console.log("Alert called with message:", message);
  };
  
  // 날짜가 유효한 YYMMDD 형식인지 검사하는 함수
  function isValidDate(dateString) {
    const regex = /^(?:[0-9]{2})(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])$/;
    return regex.test(dateString);
  }
  
  // 입력 시도 함수
  function tryPasswords() {
    const input = document.getElementById('pass');
    const button = document.querySelector('button[onclick*="0x9a220"]');
    
    // 000000부터 999999까지 모든 가능한 날짜를 시도합니다.
    for (let i = 0; i <= 999999; i--) {
      // 숫자를 문자열로 변환하고, 필요하면 앞에 0을 붙여 길이를 6으로 맞춥니다.
      const stringValue = i.toString().padStart(6, '0');
      // 유효한 날짜 형식인지 검사합니다.
      if (isValidDate(stringValue)) {
        input.value = stringValue;
        button.click();
        // 정답이면 중단하고, 아니면 계속 시도합니다.
        // 정답 확인을 위한 추가 로직이 필요할 수 있습니다.
      }
    }
  }
  
  tryPasswords(); // 함수를 호출하여 실행합니다.
  




window.alert = function ( text ) {
    console.log( 'tried to alert: ' + text );
    return true;
};

function birthday(aaa) {
    var format = /^([0-9]{2}(0[1-9]|1[0-2])(0[1-9]|[1,2][0-9]|3[0,1]))$/;
    if(format.test(aaa)) {
        _0x9a220(aaa);
    } else {
    }
}

for(var i = 800000; i < 999999; i++) {
    birthday(i);
}