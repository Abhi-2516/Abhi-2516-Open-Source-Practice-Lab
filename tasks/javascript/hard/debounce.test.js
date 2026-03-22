import debounce from './debounce.js';

console.log('=== Debounce Function Tests ===\n');

// Test 1: Basic debounce - function called after delay
console.log('Test 1: Basic debounce');
let callCount1 = 0;
const basicFn = () => {
  callCount1++;
  console.log(`Function called. Count: ${callCount1}`);
};

const debouncedBasic = debounce(basicFn, 500);
debouncedBasic();
debouncedBasic();
debouncedBasic();
console.log('Called 3 times, waiting 500ms...');

setTimeout(() => {
  console.log(`Result: Function executed ${callCount1} time(s) (expected: 1)\n`);
}, 600);

// Test 2: Multiple calls with arguments
setTimeout(() => {
  console.log('Test 2: Pass arguments to debounced function');
  let lastValue = null;
  const argFn = (value) => {
    lastValue = value;
    console.log(`Function called with: ${value}`);
  };

  const debouncedArg = debounce(argFn, 300);
  debouncedArg('first');
  debouncedArg('second');
  debouncedArg('third');
  console.log('Called with 3 different values, waiting 300ms...');

  setTimeout(() => {
    console.log(`Result: Last value was "${lastValue}" (expected: "third")\n`);
  }, 400);
}, 700);

// Test 3: Rapid calls within delay period
setTimeout(() => {
  console.log('Test 3: Rapid calls (should only execute last one)');
  let executionCount = 0;
  const rapidFn = () => {
    executionCount++;
  };

  const debouncedRapid = debounce(rapidFn, 200);
  
  // Simulate rapid user input
  for (let i = 0; i < 10; i++) {
    debouncedRapid();
  }
  console.log('Called 10 times rapidly, waiting 200ms...');

  setTimeout(() => {
    console.log(`Result: Function executed ${executionCount} time(s) (expected: 1)\n`);
  }, 300);
}, 1500);

// Test 4: Search simulation
setTimeout(() => {
  console.log('Test 4: Search simulation (typing)');
  let searchQuery = '';
  const searchFn = (query) => {
    searchQuery = query;
    console.log(`Searching for: "${query}"`);
  };

  const debouncedSearch = debounce(searchFn, 400);
  
  // Simulate typing "debounce"
  const letters = ['d', 'e', 'b', 'o', 'u', 'n', 'c', 'e'];
  let index = 0;
  
  const typeInterval = setInterval(() => {
    if (index < letters.length) {
      const word = letters.slice(0, index + 1).join('');
      console.log(`User typed: "${word}"`);
      debouncedSearch(word);
      index++;
    } else {
      clearInterval(typeInterval);
    }
  }, 100);

  setTimeout(() => {
    console.log(`Result: Final search query was "${searchQuery}" (expected: "debounce")\n`);
  }, 1500);
}, 2000);

// Test 5: Reset delay on each call
setTimeout(() => {
  console.log('Test 5: Reset delay on each call');
  let callNumber = 0;
  const resetFn = () => {
    callNumber++;
    console.log(`Function called (call #${callNumber})`);
  };

  const debouncedReset = debounce(resetFn, 300);
  
  debouncedReset();
  console.log('Call 1 at 0ms');
  
  setTimeout(() => {
    debouncedReset();
    console.log('Call 2 at 200ms (reset timer)');
  }, 200);

  setTimeout(() => {
    console.log('Waiting for execution...');
  }, 250);

  setTimeout(() => {
    console.log(`Result: Function executed ${callNumber} time(s) (expected: 1)`);
    console.log('\n=== All Tests Complete ===');
  }, 550);
}, 4000);
