"""PPQ (PayPerQ) provider profile."""

from providers import register_provider
from providers.base import ProviderProfile


ppq = ProviderProfile(
    name="ppq",
    aliases=("payperq", "ppq.ai", "pay-per-q", "pay-per-queue", "payperqueue"),
    display_name="PPQ (PayPerQ)",
    description="PPQ (PayPerQ multi-provider gateway)",
    signup_url="https://ppq.ai/",
    env_vars=("PPQ_API_KEY", "PPQ_BASE_URL"),
    base_url="https://api.ppq.ai/v1",
    auth_type="api_key",
    default_aux_model="perplexity/sonar",
    fallback_models=(
        # Curated PPQ list using PPQ's native IDs. Keep a small, agentic set;
        # the live /v1/models catalog is preferred whenever PPQ_API_KEY works.
        "gpt-5.5",
        "gpt-5.5-pro",
        "claude-opus-4.8",
        "claude-sonnet-4.6",
        "claude-haiku-4.5",
        "anthropic/claude-opus-4.8-fast",
        "anthropic/claude-opus-4.7-fast",
        "grok-4.20",
        "x-ai/grok-4.3",
        "x-ai/grok-4.20-multi-agent",
        "perplexity/sonar-pro-search",
        "perplexity/sonar-reasoning-pro",
        "perplexity/sonar-pro",
        "perplexity/sonar-deep-research",
        "perplexity/sonar",
        "google/gemini-3.5-flash",
        "gemini-3-flash-preview",
        "google/gemini-3.1-pro-preview",
        "google/gemini-3.1-flash-lite-preview",
        "qwen/qwen3.7-max",
        "qwen/qwen3.6-plus",
        "qwen/qwen3.6-flash",
        "qwen/qwen3-coder-plus",
        "qwen/qwen3-coder-flash",
        "z-ai/glm-5.1",
        "z-ai/glm-5-turbo",
        "moonshotai/kimi-k2.6",
        "moonshotai/kimi-k2.5",
        "minimax/minimax-m3",
        "minimax/minimax-m2.7",
        "xiaomi/mimo-v2.5-pro",
        "xiaomi/mimo-v2-flash",
        "deepseek/deepseek-v4-pro",
        "deepseek/deepseek-v4-flash",
        "stepfun/step-3.7-flash",
        "nvidia/nemotron-3-super-120b-a12b",
        "arcee-ai/trinity-large-thinking",
    ),
)

register_provider(ppq)
