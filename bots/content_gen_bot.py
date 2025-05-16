    import sys
    try:
                      topic = sys.argv[1] if len(sys.argv) > 1 else ''
                      style = sys.argv[2] if len(sys.argv) > 2 else ''
                      platform = sys.argv[3] if len(sys.argv) > 3 else ''
                      result = run_content_gen_task(topic, style, platform)
                      print("\n[Generated Content]:\n", result)
except Exception as e:
                  print(f"Error: {e}")
          
