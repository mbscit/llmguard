# Generated by Django 5.0.2 on 2024-04-23 17:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LlmModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('model', models.CharField(choices=[('ANYSCALE::meta-llama/Llama-2-7b-chat-hf', 'ANYSCALE::meta-llama/Llama-2-7b-chat-hf'), ('ANYSCALE::meta-llama/Llama-2-13b-chat-hf', 'ANYSCALE::meta-llama/Llama-2-13b-chat-hf'), ('ANYSCALE::meta-llama/Llama-2-70b-chat-hf', 'ANYSCALE::meta-llama/Llama-2-70b-chat-hf'), ('ANYSCALE::codellama/CodeLlama-34b-Instruct-hf', 'ANYSCALE::codellama/CodeLlama-34b-Instruct-hf'), ('ANYSCALE::mistralai/Mistral-7B-Instruct-v0.1', 'ANYSCALE::mistralai/Mistral-7B-Instruct-v0.1'), ('ANYSCALE::HuggingFaceH4/zephyr-7b-beta', 'ANYSCALE::HuggingFaceH4/zephyr-7b-beta'), ('OPENAI::gpt-3.5-turbo', 'OPENAI::gpt-3.5-turbo'), ('OPENAI::gpt-4', 'OPENAI::gpt-4'), ('TOGETHER::mistralai/Mistral-7B-v0.1', 'TOGETHER::mistralai/Mistral-7B-v0.1'), ('TOGETHER::lmsys/vicuna-7b-v1.5', 'TOGETHER::lmsys/vicuna-7b-v1.5'), ('TOGETHER::togethercomputer/CodeLlama-7b', 'TOGETHER::togethercomputer/CodeLlama-7b'), ('TOGETHER::togethercomputer/CodeLlama-7b-Python', 'TOGETHER::togethercomputer/CodeLlama-7b-Python'), ('TOGETHER::togethercomputer/CodeLlama-7b-Instruct', 'TOGETHER::togethercomputer/CodeLlama-7b-Instruct'), ('TOGETHER::togethercomputer/CodeLlama-13b', 'TOGETHER::togethercomputer/CodeLlama-13b'), ('TOGETHER::togethercomputer/CodeLlama-13b-Python', 'TOGETHER::togethercomputer/CodeLlama-13b-Python'), ('TOGETHER::togethercomputer/CodeLlama-13b-Instruct', 'TOGETHER::togethercomputer/CodeLlama-13b-Instruct'), ('TOGETHER::togethercomputer/falcon-40b', 'TOGETHER::togethercomputer/falcon-40b'), ('TOGETHER::togethercomputer/llama-2-7b', 'TOGETHER::togethercomputer/llama-2-7b'), ('TOGETHER::togethercomputer/llama-2-7b-chat', 'TOGETHER::togethercomputer/llama-2-7b-chat'), ('TOGETHER::togethercomputer/llama-2-13b', 'TOGETHER::togethercomputer/llama-2-13b'), ('TOGETHER::togethercomputer/llama-2-13b-chat', 'TOGETHER::togethercomputer/llama-2-13b-chat'), ('TOGETHER::togethercomputer/llama-2-70b', 'TOGETHER::togethercomputer/llama-2-70b'), ('TOGETHER::togethercomputer/llama-2-70b-chat', 'TOGETHER::togethercomputer/llama-2-70b-chat')], max_length=100)),
                ('api_key', models.CharField(blank=True, max_length=100, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
