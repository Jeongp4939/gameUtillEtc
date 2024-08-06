const input = prompt("Enter input: ").split(" ");
let result = parseInt(input[0]);
const nums = input.slice(1, 3).map(Number); // 12
const calc = input.slice(3, 5); // 34
const word = input[input.length - 1]; // 5

const copyToClipBoard = (data) => {
  if (navigator.clipboard) {
    // 텍스트를 클립보드에 복사
    navigator.clipboard.writeText(data)
      .then(() => {
        console.log('텍스트가 클립보드에 복사되었습니다.');
        alert(data); // 결과를 alert로 표시
      })
      .catch(err => {
        console.error('클립보드 복사 실패:', err);
      });
  } else {
    // Clipboard API를 지원하지 않는 경우 대체 처리
    console.warn('Clipboard API가 지원되지 않습니다.');
  }
}

for (let i = 0; i < 2; i++) {
  if (calc[i] === "+") {
    result += nums[i];
  } else if (calc[i] === "-") {
    result -= nums[i];
  } else if (calc[i] === "*") {
    result *= nums[i];
  }
}

result = result.toString() + word;

// Ensure document has focus before copying to clipboard
if (document.hasFocus()) {
  copyToClipBoard(result);
} else {
  window.addEventListener('focus', () => copyToClipBoard(result), { once: true });
  alert('브라우저 창에 포커스를 맞추고 다시 시도해주세요.');
}
