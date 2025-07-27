#!/usr/bin/env python3
"""
CLI tool to test and interact with the Illustrator MCP prompt system
"""

import json
import argparse
from illustrator.prompt import (
    get_prompt_suggestions,
    get_system_prompt,
    get_prompting_tips,
    get_advanced_templates,
    display_help,
    format_advanced_template
)

def main():
    parser = argparse.ArgumentParser(description="Adobe Illustrator MCP Prompt Helper")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Suggestions command
    suggestions_parser = subparsers.add_parser('suggestions', help='Get prompt suggestions')
    suggestions_parser.add_argument('--category', type=str, help='Filter by category')
    suggestions_parser.add_argument('--list-categories', action='store_true', help='List available categories')
    
    # System prompt command
    subparsers.add_parser('system-prompt', help='Get the system prompt template')
    
    # Tips command
    subparsers.add_parser('tips', help='Get prompting tips')
    
    # Templates command
    templates_parser = subparsers.add_parser('template', help='Get advanced templates')
    templates_parser.add_argument('--type', type=str, help='Template type (logo_design, illustration, infographic, icon_set)')
    templates_parser.add_argument('--list-types', action='store_true', help='List available template types')
    templates_parser.add_argument('--params', type=str, help='JSON string of parameters to fill template')
    
    # Help command
    subparsers.add_parser('help', help='Display comprehensive help')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    if args.command == 'suggestions':
        suggestions = get_prompt_suggestions()
        
        if args.list_categories:
            print("Available categories:")
            for category in suggestions.keys():
                print(f"  - {category}")
            return
        
        if args.category:
            # Find matching category
            matching_category = None
            for category in suggestions.keys():
                if args.category.lower() in category.lower():
                    matching_category = category
                    break
            
            if matching_category:
                print(f"\n{matching_category}")
                print("=" * len(matching_category))
                for suggestion in suggestions[matching_category]:
                    print(f"• {suggestion}")
            else:
                print(f"Category '{args.category}' not found.")
                print("Available categories:")
                for category in suggestions.keys():
                    print(f"  - {category}")
        else:
            print("🎨 All Prompt Suggestions")
            print("=" * 25)
            for category, prompts in suggestions.items():
                print(f"\n{category}")
                print("-" * len(category))
                for prompt in prompts[:3]:  # Show first 3 to avoid overwhelming
                    print(f"• {prompt}")
                if len(prompts) > 3:
                    print(f"  ... and {len(prompts) - 3} more")
    
    elif args.command == 'system-prompt':
        print(get_system_prompt())
    
    elif args.command == 'tips':
        tips = get_prompting_tips()
        print("💡 Prompting Tips for Adobe Illustrator")
        print("=" * 40)
        for tip in tips:
            print(tip)
    
    elif args.command == 'template':
        templates = get_advanced_templates()
        
        if args.list_types:
            print("Available template types:")
            for template_type in templates.keys():
                print(f"  - {template_type}")
            return
        
        if args.type:
            if args.type in templates:
                template = templates[args.type]
                
                if args.params:
                    try:
                        params = json.loads(args.params)
                        formatted_template = format_advanced_template(args.type, **params)
                        print(formatted_template)
                    except json.JSONDecodeError:
                        print("Error: Invalid JSON in --params")
                    except KeyError as e:
                        print(f"Error: Missing required parameter: {e}")
                        print(f"\nTemplate with placeholders:")
                        print(template)
                else:
                    print(f"{args.type.replace('_', ' ').title()} Template:")
                    print("=" * 30)
                    print(template)
            else:
                print(f"Template '{args.type}' not found.")
                print("Available templates:")
                for template_type in templates.keys():
                    print(f"  - {template_type}")
        else:
            print("Available advanced templates:")
            for template_type in templates.keys():
                print(f"\n{template_type.replace('_', ' ').title()}:")
                print(f"  Use: python prompt_cli.py template --type {template_type}")
    
    elif args.command == 'help':
        print(display_help())

if __name__ == "__main__":
    main()
