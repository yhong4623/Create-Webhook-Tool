# Webhook創建工具

一個使用 `discord.py` 開發的 Discord 機器人，支援透過斜線指令在指定分類中創建文字頻道和 Webhook。機器人提供兩個主要指令：`/set_category` 用於設置目標分類 ID，`/create_channel` 用於創建新的頻道和 Webhook。

## 功能

- **斜線指令**：
  - `/set_category <category_id>`：設置用於創建頻道的分類 ID。
  - `/create_channel <channel_name>`：在指定分類中創建文字頻道和 Webhook。
- **模組化設計**：使用 cogs 和工具模組組織程式碼，便於維護。
- **錯誤處理**：驗證分類 ID、權限，並處理 HTTP 錯誤。
- **隱私回應**：所有指令回應僅對執行者可見（ephemeral）。
- **動態分類管理**：透過指令設置分類 ID，並驗證是否為有效分類頻道。

## 前置條件

- Python 3.8 或更高版本
- Discord 機器人 Token（可透過 [Discord 開發者入口](https://discord.com/developers/applications) 創建）
- `discord.py` 函式庫

## 安裝

1. **複製儲存庫**：
   ```bash
   git clone https://github.com/your-username/discord-channel-bot.git
   cd discord-channel-bot
   ```

2. **設置虛擬環境**（建議但非必須）：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows 上：venv\Scripts\activate
   ```

3. **安裝依賴**：
   ```bash
   pip install discord.py
   ```

4. **配置機器人 Token**：
   - 打開 `main.py`，將 `'YOUR_BOT_TOKEN'` 替換為您的 Discord 機器人 Token。

## 專案結構

```
discord-channel-bot/
├── main.py                # 機器人初始化和 cog 載入
├── cogs/
│   └── channel_commands.py # 設置分類和創建頻道的斜線指令
├── utils/
│   └── config.py          # 分類 ID 管理
├── README.md              # 專案說明文件
```

## 使用方法

1. **運行機器人**：
   ```bash
   python main.py
   ```

2. **邀請機器人**：
   - 確保機器人具有必要權限（`管理頻道` 和 `管理 Webhook`）。
   - 在 Discord 開發者入口生成 OAuth2 邀請連結（啟用 `bot` 和 `applications.commands` 範圍），將機器人邀請至您的伺服器。

3. **使用斜線指令**：
   - **設置分類 ID**：
     ```
     /set_category <category_id>
     ```
     範例：`/set_category 123456789012345678`
     - 設置用於創建頻道的目標分類。
     - 會驗證 ID 是否對應有效的分類頻道。

   - **創建頻道和 Webhook**：
     ```
     /create_channel <channel_name>
     ```
     範例：`/create_channel my-new-channel`
     - 在設定的分類中創建文字頻道和 Webhook。
     - 需先使用 `/set_category` 設置分類 ID。

4. **注意事項**：
   - 指令回應為隱私模式（僅執行者可見）。
   - 若未設置分類 ID，`/create_channel` 會提示使用 `/set_category`。
   - 分類 ID 儲存在記憶體中，機器人重啟後需重新設置。如需持久化儲存，可考慮使用資料庫或檔案。

## 範例流程

1. 運行機器人並邀請至您的伺服器。
2. 使用 `/set_category 123456789012345678` 設置目標分類。
3. 使用 `/create_channel my-channel` 創建名為 "my-channel" 的頻道和 Webhook。
4. 收到包含頻道提及和 Webhook URL 的 Embed（僅您可見）。

## 疑難排解

- **斜線指令未出現**：
  - 確認邀請連結包含 `applications.commands` 範圍。
  - 等待數分鐘讓 Discord 同步指令，或在程式碼中重新執行 `bot.tree.sync()`。
- **權限錯誤**：
  - 檢查機器人是否具有 `管理頻道` 和 `管理 Webhook` 權限。
- **無效分類 ID**：
  - 確保輸入的 ID 對應伺服器中的分類頻道。

## 貢獻

歡迎提交問題或拉取請求！請遵循以下步驟：
1. Fork 儲存庫。
2. 創建您的功能分支（`git checkout -b feature/YourFeature`）。
3. 提交變更（`git commit -m 'Add YourFeature'`）。
4. 推送到分支（`git push origin feature/YourFeature`）。
5. 開啟拉取請求。

## 授權

本專案採用 [MIT 授權](LICENSE)。詳情請見 `LICENSE` 檔案。
