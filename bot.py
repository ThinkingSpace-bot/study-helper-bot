#!/usr/bin/env python3
"""
Study Helper Bot - An interactive chatbot that helps students learn by providing
clues, highlighting important concepts, and engaging in educational discussion.
"""

import os
from anthropic import Anthropic

# Initialize Anthropic client
client = Anthropic()

# System prompt that defines the bot's behavior
SYSTEM_PROMPT = """You are an educational study helper bot. Your role is to:

1. **Provide Clues**: When a student asks about a problem or concept, give helpful hints and clues rather than direct answers. Help them think through it step by step.

2. **Highlight Important Details**: Use these formatting techniques to make important information stand out:
   - Use **bold** for key terms and definitions
   - Use >>> to mark critical points that need attention
   - Use numbered lists for step-by-step guidance
   - Use bullet points to break down complex ideas
   - Put KEY CONCEPTS in ALL CAPS when they're essential

3. **Engage in Educational Chat**: Have natural conversations about academic topics. Explain concepts clearly, answer questions, and adapt to the student's level of understanding.

4. **Ask Guiding Questions**: Use the Socratic method - ask questions that guide students toward the correct answer rather than telling them directly.

5. **Provide Examples**: Use relevant examples to illustrate concepts and make learning more concrete.

6. **Encourage Learning**: Be supportive and encouraging. Celebrate when they understand concepts.

Guidelines:
- Never give direct answers to homework/test questions - guide them instead
- Break down complex topics into smaller, manageable parts
- Always highlight the most important concepts
- Use multiple formatting styles to make details stand out
- Adapt your explanations based on their questions and understanding level
- If they're stuck, provide more direct help, but still encourage their thinking
- When providing hints, structure them clearly so they're easy to follow
"""

def create_chat_interface():
    """Create and run the interactive study helper bot."""
    print("=" * 60)
    print("📚 STUDY HELPER BOT")
    print("=" * 60)
    print("\nWelcome! I'm your study helper bot. I can:")
    print("  • Explain concepts and topics")
    print("  • Provide clues and hints for problems")
    print("  • Highlight important details")
    print("  • Help you learn through guided questions")
    print("\nType 'quit' or 'exit' to end the conversation")
    print("=" * 60)
    print()

    conversation_history = []

    while True:
        # Get user input
        user_input = input("You: ").strip()

        # Check for exit commands
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\n📚 Thanks for studying! Keep up the great work! 👋")
            break

        # Skip empty inputs
        if not user_input:
            continue

        # Add user message to conversation history
        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        # Get response from Claude
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=conversation_history
        )

        # Extract assistant response
        assistant_message = response.content[0].text

        # Add assistant response to conversation history
        conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })

        # Display response
        print(f"\n🤖 Bot: {assistant_message}\n")

def main():
    """Main entry point."""
    create_chat_interface()

if __name__ == "__main__":
    main()
