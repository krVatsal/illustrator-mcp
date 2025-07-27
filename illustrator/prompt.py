"""
Prompt templates and suggestions for Adobe Illustrator MCP Server
"""

# System prompt template for better user guidance
SYSTEM_PROMPT_TEMPLATE = """
You are an AI assistant that can control Adobe Illustrator through ExtendScript/JavaScript. 
You can create vector graphics, illustrations, logos, and designs directly in Illustrator.

CAPABILITIES:
- Create shapes, paths, and vector graphics
- Apply colors, gradients, and effects
- Manipulate text and typography
- Work with layers and artboards
- Import/export files
- Apply transformations and effects

BEST PRACTICES:
- Always describe what you're creating before executing
- Use specific measurements and coordinates when possible
- Consider color theory and design principles
- Test simple shapes before complex illustrations
- Use meaningful names for layers and objects

EXTENDSCRIPT TIPS:
- Use app.activeDocument to access the current document
- Create new documents with app.documents.add()
- Use pathItems.rectangle(), pathItems.ellipse() for basic shapes
- Access colors through app.activeDocument.swatches
- Use textFrames.add() for text elements
"""

# Prompt suggestion categories
PROMPT_SUGGESTIONS = {
    "🎨 Basic Shapes & Geometry": [
        "Create a circle with a 5-inch diameter, filled with blue color",
        "Draw a golden rectangle using the golden ratio proportions",
        "Make a hexagon with equal sides, outlined in black, filled with gradient from red to orange",
        "Create a triangle with rounded corners and a drop shadow effect",
        "Design a star shape with 8 points and apply a metallic gradient"
    ],
    
    "📝 Typography & Text": [
        "Create a modern logo text saying 'TechCorp' using a bold sans-serif font",
        "Design a vintage-style typography poster with the text 'Coffee Shop' in brown tones",
        "Make a text effect with 'NEON' that looks like glowing neon lights",
        "Create a 3D text effect for the word 'FUTURE' with metallic finish",
        "Design a handwritten-style text saying 'Welcome' with decorative flourishes"
    ],
    
    "🏢 Logos & Branding": [
        "Design a minimalist logo for a photography studio called 'LensArt'",
        "Create a modern tech company logo incorporating circuit patterns",
        "Design a coffee shop logo with a steaming cup and warm colors",
        "Make a fitness brand logo with dynamic, energetic elements",
        "Create a nature-inspired logo for an eco-friendly company"
    ],
    
    "🌆 Illustrations & Scenes": [
        "Create a flat design illustration of a city skyline at sunset",
        "Design a vector illustration of a peaceful forest scene with animals",
        "Make a minimalist mountain landscape with geometric shapes",
        "Create an isometric illustration of a modern office workspace",
        "Design a space scene with planets, stars, and a rocket ship"
    ],
    
    "🎭 Icons & UI Elements": [
        "Create a set of 5 social media icons in a consistent style",
        "Design weather icons: sun, cloud, rain, and snow",
        "Make a collection of navigation icons for a mobile app",
        "Create business icons: chart, briefcase, handshake, lightbulb",
        "Design food icons in a flat, colorful style"
    ],
    
    "🎨 Artistic & Creative": [
        "Create an abstract geometric pattern with vibrant colors",
        "Design a mandala pattern with intricate details and symmetry",
        "Make a watercolor-style illustration (using vector techniques)",
        "Create a vintage poster design for a music festival",
        "Design a modern art piece inspired by cubism"
    ],
    
    "📊 Charts & Infographics": [
        "Create a pie chart showing market share data with labels",
        "Design a bar chart comparing quarterly sales figures",
        "Make an infographic about renewable energy with icons and stats",
        "Create a flowchart for a simple business process",
        "Design a timeline infographic for historical events"
    ],
    
    "🏷️ Print & Layout": [
        "Design a business card layout with company information",
        "Create a flyer design for a summer sale event",
        "Make a book cover design for a mystery novel",
        "Design a magazine layout with text and image placeholders",
        "Create a poster design for a charity fundraising event"
    ]
}

# Advanced prompt templates for complex tasks
ADVANCED_PROMPT_TEMPLATES = {
    "logo_design": """
    Design a professional logo for {company_name} in the {industry} industry.
    
    Requirements:
    - Style: {style} (modern, vintage, minimalist, etc.)
    - Colors: {colors}
    - Include: {elements}
    - Size: {size}
    - Format: Vector format suitable for scalability
    
    Please create the logo step by step, explaining each design decision.
    """,
    
    "illustration": """
    Create a {style} illustration of {subject}.
    
    Specifications:
    - Art style: {art_style}
    - Color palette: {colors}
    - Mood: {mood}
    - Level of detail: {detail_level}
    - Background: {background}
    
    Start with basic shapes and build up the complexity gradually.
    """,
    
    "infographic": """
    Design an infographic about {topic}.
    
    Content structure:
    - Title: {title}
    - Key statistics: {stats}
    - Visual elements: {visual_elements}
    - Color scheme: {colors}
    - Target audience: {audience}
    
    Use icons, charts, and visual hierarchy to make the information engaging.
    """,
    
    "icon_set": """
    Create a set of {number} icons for {purpose}.
    
    Icon specifications:
    - Style: {style} (flat, outline, filled, etc.)
    - Size: {size}
    - Color scheme: {colors}
    - Icons needed: {icon_list}
    - Consistency: Maintain visual consistency across all icons
    
    Design each icon to be clear and recognizable at small sizes.
    """
}

# Tips for better prompting
PROMPTING_TIPS = [
    "🎯 Be specific about dimensions, colors, and positioning",
    "📐 Use exact measurements when precision matters",
    "🎨 Describe the art style or aesthetic you want",
    "📝 Break complex requests into smaller steps",
    "🔄 Ask for iterations and refinements",
    "📋 Specify file format and export requirements",
    "🎭 Mention the intended use case or context",
    "🔍 Request previews before finalizing complex designs",
    "📊 Provide reference examples when possible",
    "⚡ Start simple and add complexity gradually"
]

def get_system_prompt() -> str:
    """Get the system prompt template for better AI guidance."""
    return SYSTEM_PROMPT_TEMPLATE

def get_prompt_suggestions() -> dict:
    """Get categorized prompt suggestions."""
    return PROMPT_SUGGESTIONS

def get_advanced_templates() -> dict:
    """Get advanced prompt templates for complex tasks."""
    return ADVANCED_PROMPT_TEMPLATES

def get_prompting_tips() -> list:
    """Get tips for better prompting."""
    return PROMPTING_TIPS

def format_advanced_template(template_name: str, **kwargs) -> str:
    """Format an advanced template with provided parameters."""
    if template_name in ADVANCED_PROMPT_TEMPLATES:
        return ADVANCED_PROMPT_TEMPLATES[template_name].format(**kwargs)
    else:
        raise ValueError(f"Template '{template_name}' not found")

def display_help() -> str:
    """Display comprehensive help information."""
    help_text = """
    🎨 ADOBE ILLUSTRATOR MCP SERVER HELP 🎨
    
    This server allows you to control Adobe Illustrator using natural language.
    You can create vector graphics, illustrations, logos, and designs.
    
    📋 QUICK START:
    1. Make sure Adobe Illustrator is running
    2. Use natural language to describe what you want to create
    3. The AI will generate ExtendScript code to execute in Illustrator
    4. View results using the screenshot feature
    
    💡 PROMPTING TIPS:
    """
    
    for tip in PROMPTING_TIPS:
        help_text += f"\n    {tip}"
    
    help_text += "\n\n📚 EXAMPLE CATEGORIES:\n"
    
    for category in PROMPT_SUGGESTIONS.keys():
        help_text += f"\n    {category}"
    
    help_text += "\n\n🔧 Use 'get_prompt_suggestions()' to see specific examples!"
    
    return help_text
