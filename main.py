from agent import agent


def main():
    print("Research Agent with RAG (type 'exit' to quit)")
    print("-" * 40)

    config = {"configurable": {"thread_id": "interactive-session-1"}}

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        final_answer = None
        seen_tool_calls = set()
        seen_tool_results = set()

        for step in agent.stream(
            {"messages": [("user", user_input)]},
            config=config,
            stream_mode="values",
        ):
            messages = step.get("messages", [])
            if not messages:
                continue

            last_msg = messages[-1]

            tool_calls = getattr(last_msg, "tool_calls", None)
            if tool_calls:
                for call in tool_calls:
                    tool_name = call.get("name", "unknown_tool")
                    tool_args = str(call.get("args", {}))
                    key = (tool_name, tool_args)
                    if key not in seen_tool_calls:
                        seen_tool_calls.add(key)
                        print(f"\n🔧 Tool call: {tool_name}({tool_args})")

            if getattr(last_msg, "type", "") == "tool":
                content = getattr(last_msg, "content", "")
                if content not in seen_tool_results:
                    seen_tool_results.add(content)
                    preview = content[:500] + ("..." if len(content) > 500 else "")
                    print(f"\n📎 Result: {preview}")

            if getattr(last_msg, "type", "") == "ai" and getattr(last_msg, "content", ""):
                final_answer = last_msg.content

        if final_answer:
            print(f"\nAgent:\n{final_answer}")
        else:
            print("\nAgent: No final response generated.")


if __name__ == "__main__":
    main()