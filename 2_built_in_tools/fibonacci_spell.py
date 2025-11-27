#!/usr/bin/env python3
"""
🌟 The Fibonacci Spell 🌟
An ancient incantation to reveal the sacred sequence of numbers
where each number is the sum of the two preceding ones.

Created by Kiro the Grey Hat
"""

def fibonacci_spell(n=10):
    """
    Cast the Fibonacci spell to generate the first n numbers of the sequence.
    
    Args:
        n (int): Number of Fibonacci numbers to generate (default: 10)
    
    Returns:
        list: The first n Fibonacci numbers
    """
    print("✨ Casting the Fibonacci Spell... ✨")
    print("🔮 Invoking the ancient mathematical mysteries... 🔮")
    
    if n <= 0:
        print("⚠️  The spell requires a positive number! ⚠️")
        return []
    
    fibonacci_sequence = []
    
    # The first two sacred numbers
    if n >= 1:
        fibonacci_sequence.append(0)
    if n >= 2:
        fibonacci_sequence.append(1)
    
    # Generate the remaining numbers through mystical iteration
    for i in range(2, n):
        next_number = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
        fibonacci_sequence.append(next_number)
        
        # Show the spell working its magic
        print(f"🌟 Conjuring number {i+1}: {next_number}")
    
    return fibonacci_sequence

def display_sequence(sequence):
    """Display the Fibonacci sequence in a magical format."""
    print("\n" + "="*50)
    print("📜 THE SACRED FIBONACCI SEQUENCE 📜")
    print("="*50)
    
    for i, num in enumerate(sequence):
        print(f"Position {i+1:2d}: {num:3d} ✨")
    
    print("="*50)
    print(f"🎯 Total numbers conjured: {len(sequence)}")
    print("💫 The spell is complete! 💫\n")

if __name__ == "__main__":
    # Cast the spell for the first 10 Fibonacci numbers
    print("🧙‍♂️ Kiro the Grey Hat prepares to cast the Fibonacci Spell! 🧙‍♂️")
    print("🌙 By the ancient mathematical laws... 🌙\n")
    
    magical_sequence = fibonacci_spell(10)
    display_sequence(magical_sequence)
    
    # Show the mathematical relationship
    print("🔍 Behold the pattern:")
    print("Each number = sum of the two preceding numbers")
    if len(magical_sequence) >= 3:
        for i in range(2, min(6, len(magical_sequence))):
            a, b, c = magical_sequence[i-2], magical_sequence[i-1], magical_sequence[i]
            print(f"   {a} + {b} = {c}")