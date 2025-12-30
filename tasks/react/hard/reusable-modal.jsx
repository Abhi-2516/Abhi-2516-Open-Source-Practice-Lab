/*
TASK: Reusable Modal Component

Requirements:
- Accept props: isOpen, onClose
- Render children
- Close on button click
*/

function Modal({ isOpen, onClose, children }) {
  // TODO: Implement modal logic

  if (!isOpen) return null;

  return (
    <div>
      <button onClick={onClose}>Close</button>
      {children}
    </div>
  );
}

export default Modal;
